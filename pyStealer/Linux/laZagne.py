#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##############################################################################
#                                                                            #
#                           By Alessandro ZANNI                              #
#                                                                            #
##############################################################################

# Disclaimer: Do Not Use this program for illegal purposes ;)

import sys
import os
import argparse
import logging

from lazagne.config.write_output import write_in_file, StandardOutput
from lazagne.config.manage_modules import get_categories
from lazagne.config.constant import constant
from lazagne.config.run import create_module_dic, run_lazagne

import time

constant.st = StandardOutput()  # Object used to manage the output / write functions (cf write_output file)
modules = create_module_dic()


def output(output_dir=None, txt_format=False, json_format=False, all_format=False):
    if output_dir:
        if os.path.isdir(output_dir):
            constant.folder_name = output_dir
        else:
            print('[!] Specify a directory, not a file !')

    if txt_format:
        constant.output = 'txt'

    if json_format:
        constant.output = 'json'

    if all_format:
        constant.output = 'all'

    if constant.output:
        if not os.path.exists(constant.folder_name):
            os.makedirs(constant.folder_name)
            # constant.file_name_results = 'credentials' # let the choice of the name to the user

        if constant.output != 'json':
            constant.st.write_header()


def quiet_mode(is_quiet_mode=False):
    if is_quiet_mode:
        constant.quiet_mode = True


def verbosity(verbose=0):
    # Write on the console + debug file
    if verbose == 0:
        level = logging.CRITICAL
    elif verbose == 1:
        level = logging.INFO
    elif verbose >= 2:
        level = logging.DEBUG

    formatter = logging.Formatter(fmt='%(message)s')
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(level)
    # If other logging are set
    for r in root.handlers:
        r.setLevel(logging.CRITICAL)
    root.addHandler(stream)


def clean_args(arg):
    """
    Remove not necessary values to get only subcategories
    """
    for i in ['output', 'write_normal', 'write_json', 'write_all', 'verbose', 'auditType', 'quiet']:
        try:
            del arg[i]
        except Exception:
            pass
    return arg


def runLaZagne(category_selected='all', subcategories={}):
    """
    This function will be removed, still there for compatibility with other tools
    Everything is on the config/run.py file
    """
    yield from run_lazagne(
        category_selected=category_selected, subcategories=subcategories
    )


if __name__ == "__main__":
    quiet_mode(is_quiet_mode=True)

    import platform

    try:
        kullanici_adi = os.getlogin()
    except OSError:
        import pwd
        kullanici_adi = pwd.getpwuid(os.geteuid())[0]

    bilgisayar_adi = platform.node()
    oturum = kullanici_adi + "@" + bilgisayar_adi

    from json import dumps, loads

    sifreler = {}
    for veri in runLaZagne('all', clean_args({})):
        if veri[2]:
            for bilgi in veri[2]:
                for key, value in bilgi.items():
                    if isinstance(value, bytes):
                        bilgi[key] = value.decode("utf8")
                    elif "{" in value:
                        bilgi[key] = loads(value)

        sifreler[veri[1]] = veri[2]

    with open(f'{oturum}.json', "w+", encoding='utf-8') as dosya:
        dosya.write(dumps(sifreler, indent=2, ensure_ascii=False, sort_keys=True))