#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
import os
import logging
import subprocess
import argparse
from distutils import dir_util


def start_grip_server(source_file, target_folder):
    html_file = os.path.join(target_folder, "resume.html")
    process = subprocess.Popen(['grip', source_file, '--export', html_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait(timeout=3)
    with open(html_file, 'r') as f:
        content = f.read()
    with open(html_file, 'w') as f:
        content = remove_title(content)
        content = insert_custom_css(content)
        f.write(content)
    return html_file

def close_grip_server(process):
    process.terminate()


def remove_title(content):
    pa = re.compile(r"<h3.*?octicon octicon-book.*?h3>", re.DOTALL)
    return re.sub(pa, "", content)

def insert_custom_css(content):
    body_end = next(re.finditer(r"</body>", content))
    content = content[:body_end.start()] + """
    <script type="text/javascript">
        var linka = document.createElement("link");
        linka.href = "media/cv-print.css";
        linka.type = "text/css";
        linka.rel = "stylesheet";
        linka.media = "screen,print";
        document.getElementsByTagName( "head" )[0].appendChild(linka);

        var linkb = document.createElement("link");
        linkb.href = "media/foundation-icons/foundation-icons.css";
        linkb.type = "text/css";
        linkb.rel = "stylesheet";
        linkb.media = "screen,print";
        document.getElementsByTagName( "head" )[0].appendChild(linkb);
    </script>
    """ + content[body_end.start():]
    t_pa = re.compile(r"<h1.*?Bowen Zhi.*?h1>", re.DOTALL)
    title_end = next(re.finditer(t_pa, content))
    content = content[:title_end.end()] + """
        <div id="contact-info">
        <i class="fi-home" style="margin-left:1em"></i>
        <a href="https://www.linkedin.com/in/bowen-zhi-878756112/" style="margin-left:0.5em"> LinkedIn</a>
        <i class="fi-mail" style="margin-left:1em"></i>
        <a href="zhi.b@husky.neu.edu" style="margin-left:0.5em">zhi.b@husky.neu.edu</a>
        <i class="fi-social-github" style="margin-left:1em"></i>
        <a href="https://github.com/zz920" style="margin-left:0.5em">zz920</a>
        <i class="fi-telephone" style="margin-left:1em">+971504388108</i>
        </div>
    """ + content[title_end.end():]
    return content

def generate_pdf_file(html_file, pdf_file):
    process = subprocess.Popen("wkhtmltopdf -T 0 {} {}".format(html_file, pdf_file), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate(timeout=3)
    process.terminate()


def process(source, target, format):
    source_file = os.path.abspath(source)
    if not os.path.isfile(source_file):
        print("The input file {} not exists, please input a valid markdown file!".format(source))
        return False

    target_folder = os.path.abspath(target)
    if not os.path.isdir(target_folder):
        print("The output folder {} not exists, please input a valid folder!".format(target))
        return False
    static_file = dir_util.copy_tree("./media", os.path.join(target_folder, "media"))
    try:
        html_file = start_grip_server(source_file, target_folder)
    except Exception as e:
        print(e)
        return False

    if format == "html":
        print("The resume located in {}, please check".format(html_file))
        return True

    pdf_file = os.path.join(target_folder, "resume.pdf")
    generate_pdf_file(html_file, pdf_file)

    if not os.path.isfile(pdf_file):
        print("FAILED TO GENERATE THE PDF!")
    # os.remove(html_file)
    # os.remove(static_file)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Resume")
    parser.add_argument("-f", "--format", type=str, default='pdf', help="output format, accept html or pdf.")
    parser.add_argument("source", type=str, help="the source markdown file")
    parser.add_argument("target_folder", type=str, help="the output file folder")

    args = parser.parse_args()
    if process(args.source, args.target_folder, args.format):
        print("Done.")
    else:
        print("Wasted.")
