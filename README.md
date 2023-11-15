# Dadata API Console Application

A console application utilizing the Dadata API for address suggestions.

## Features

- **Geolocation Suggestions:** Utilize the Dadata API to get geolocation of an address using suggestions based on user input.

## Getting Started

```bash
# Clone the Repository
git clone https://github.com/Swedwish/DadataApiConsoleApplication.git

# Install Dependencies
cd DadataApiConsoleApplication
pip install -r requirements.txt
```
## Configure API Key:
Obtain an API key from Dadata and update app settings with your key.
```python
# config.py
settings
api_key {your_api_key}
```
## Usage
```bash
# Run the application
python main.py
```
### Configuration
#### Use 'settings' command to configure this application. Settings are:
* api_token {your_dadata_api_token} Use it to set your api token.
* max_count {number_from_1_to_20} Use it to set max number of results returned by dadata. Default - 10.
* language {"ru"_or_"en"} Use it to set language of the response from dadata. Does not affect language of the app. Default - "ru".

### Queries
#### Use 'dd' {address} or 'dadata' {address} command to make a call to dadata to get its' geolocation.

### Quitting
#### Use command 'q' or 'e' or 'exit' to finish work of the application. This is the prefferable way to do this.

### Help
#### Use 'help' command in app to get help.

## Contributing
1. Fork the repository.
2. Create a new branch for your changes.
3. Make changes and commit them.
4. Push changes to your fork.
5. Submit a pull request.
