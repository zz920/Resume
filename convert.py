#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
import os
import logging
import subprocess
import argparse
from distutils import dir_util
from pywebcopy import save_website


def start_grip_server(source_file):
    process = subprocess.Popen(['grip', source_file])
    # wait for server start
    time.sleep(0.5)
    if not process.poll():
        return process
    return None


def close_grip_server(process):
    process.terminate()


def remove_title(content):
    pa = re.compile(r"<h3.*?octicon octicon-book.*?h3>", re.DOTALL)
    return re.sub(pa, "", content)


def generate_html_file(target_folder):
    html_file = os.path.join(target_folder, "resume.html")
    logging.getLogger().disabled = True
    import ipdb; ipdb.set_trace()
    save_website("http://localhost:6419", "/tmp", "resume")
    static_file = os.path.join(target_folder, "__")
    dir_util.copy_tree("/tmp/resume/localhost/__", static_file)
    
    with open(html_file, 'w') as f:
        with open("/tmp/resume/localhost/index.html", 'r') as tmpf:
            content = tmpf.read()
        content = remove_title(content)
        f.write(content)

    dir_util.remove_tree("/tmp/resume")
    return html_file


def generate_pdf_file(html_file, pdf_file):
    subprocess.run("wkhtmltopdf {} {}".format(html_file, pdf_file), shell=True)


def process(source, target, format): 
    source_file = os.path.abspath(source)
    if not os.path.isfile(source_file):
        print("The input file {} not exists, please input a valid markdown file!".format(source))
        return False 
    
    target_folder = os.path.abspath(target)
    if not os.path.isdir(target_folder):
        print("The output folder {} not exists, please input a valid folder!".format(target))
        return False 

    process = start_grip_server(source_file)
    if not process:
        return False
    try:
        html_file = generate_html_file(target_folder)
    except:
        return False
    finally:
        close_grip_server(process)

    if format == "html":
        print("The resume located in {}, please check".format(html_file))
        return True
    
    pdf_file = os.path.join(target_folder, "resume.pdf")
    generate_pdf_file(html_file, pdf_file)
    if not os.path.isfile(pdf_file):
        print("FAILED TO GENERATE THE PDF!")

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
