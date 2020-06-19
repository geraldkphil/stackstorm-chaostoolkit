[![Build Status](https://circleci.com/gh/StackStorm-Exchange/stackstorm-chaostoolkit.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/StackStorm-Exchange/stackstorm-chaostoolkit) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# chaostoolkit integration pack v0.0.1

> StackStorm integration pack for Chaostoolkit
Martez Reed <martez.reed@greenreedtech.com>

[ChaosToolkit](https://chaostoolkit.org/)

# <a name="QuickStart"></a> Quick Start

Install the pack

``` shell
st2 pack install chaostoolkit
```

## Configuration

There are currently no configuration parameters.

## Actions


The pack provides the following actions:

### load_experiment
_Load experiment_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `path` | string | True | default | _The system path of the experiment_ |


### load_experiment
_Load experiment_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `path` | string | True | default | _The system path of the experiment_ |


### discover
_Run discovery_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `extension` | string | True | default | _The name of the extension to install_ |


### uninstall_extension
_Uninstall extension_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `extension` | string | True | default | _The name of the extension to uninstall_ |


### run_experiment
_Run experiment_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `path` | string | True | default | _The system path of the experiment_ |


### list_installed_extensions
_List the installed chaostoolkit extensions_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|


### install_extension
_Install extension_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `extension` | string | True | default | _The name of the extension to install_ |

## Sensors

There are no sensors available for this pack.


<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)</sub>