# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import stat
from six.moves import configparser

from azure.cli.core._environment import get_config_dir

from knack.config import get_config_parser, CLIConfig

GLOBAL_CONFIG_DIR = get_config_dir()
CONFIG_FILE_NAME = 'config'
GLOBAL_CONFIG_PATH = os.path.join(GLOBAL_CONFIG_DIR, CONFIG_FILE_NAME)
ENV_VAR_PREFIX = 'AZURE_'
DEFAULTS_SECTION = 'defaults'
