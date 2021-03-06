# Waveform and Station Downloading Client

This tool was created to automate waveform and station data download. Please cite appropriate authorities if you are using the data for non-commercial purposes. Commercial use of the data without permission is forbidden. Please read the printed warnings from the data centers printed out.

## Installation

```sh
pip install numpy==1.8.1 # obspy 1.2.1 is not compatible with numpy 1.9.1
pip install afdcli
```

## Station Data
```
get_stations(network, station, starttime, endtime, **kwargs)
```
Arguments:

`network`: Network code, wildcards allowed (`"T?"`, `"*"`)

`station`: Station code, wildcards allowed (`"B?ZM"`, `"B*"`)

`starttime`: start time string in ISO format at UTC (`"2020-03-27T06:00:13Z"`)

`endtime`: start time string in ISO format at UTC (`"2020-03-28T06:00:13Z"`)

Parameters:

`attach_response`: Returns instrument response

`minlatitude`, `maxlatitude`, `minlongitude`, `maxlongitude`: Window of coordinates of stations

## Waveform Data
```
get_waveforms(network, station, starttime, endtime, **kwargs)
```
Arguments:

`network`: Network code, wildcards allowed (`"T?"`, `"*"`)

`station`: Station code, wildcards allowed (`"B?ZM"`, `"B*"`)

`starttime`: start time string in ISO format at UTC (`"2020-03-27T06:00:13Z"`)

`endtime`: start time string in ISO format at UTC (`"2020-03-28T06:00:13Z"`)

Parameters:

`minlatitude`, `maxlatitude`, `minlongitude`, `maxlongitude`: Window of coordinates of stations

`data_format`: `"mseed"` for miniseed or `"fseed"` for fullseed formats

`filename`: filename to save the file (not implemented)


# Examples

downloading waveforms:
```
from afdcli.client import Client
c = Client()
c.get_waveforms('*','BO*', '2020-06-25T17:19:16Z', '2020-06-26T17:20:16Z')
```

downloading stations with instrument response
```
from afdcli.client import Client
c = Client()
c.get_stations('*','BO*', '2020-06-25T17:19:16Z', '2020-06-26T17:20:16Z', instrument_response=True)
```
