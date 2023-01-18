# FileShare
A simple Flask to share file through unique link

## Installation
`pip3 install -r requirements.txt`

## Usage
* run `mk_unique_folder.py test` to generate a unique folder. The argument `test` is just a hint for memorize, saved in share/match.txt
* put your file in the above generated folder
* run `python3 app.py` to start the server
* download through url: http://**your\_ip\_address**:5000/download/**unique_folder**
