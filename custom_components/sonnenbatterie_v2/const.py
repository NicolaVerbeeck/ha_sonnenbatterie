import logging
import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers import config_validation as cv
from homeassistant.const import (
    CONF_TOKEN,
    CONF_NAME,
    CONF_IP_ADDRESS,
    CONF_SCAN_INTERVAL
)
LOGGER = logging.getLogger(__package__)

DOMAIN = "sonnenbatteriev2"
DEFAULT_SCAN_INTERVAL = 10

CONFIG_SCHEMA_A=vol.Schema(
            {
                vol.Required(CONF_TOKEN): str,
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Required(CONF_NAME): str,
            }
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: CONFIG_SCHEMA_A
    },
    extra=vol.ALLOW_EXTRA,
)

ATTR_SONNEN_DEBUG = "sonnenbatterie_v2_debug"
DEFAULT_SONNEN_DEBUG = False

def flattenObj(prefix,seperator,obj):
    result={}
    for field in obj:
        val=obj[field]
        valprefix=prefix+seperator+field
        if type(val) is dict:
            sub=flattenObj(valprefix,seperator,val)
            result.update(sub)
        else:
            result[valprefix]=val
    return result
