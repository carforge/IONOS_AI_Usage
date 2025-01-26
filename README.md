**IONOS Billing API Utilization Tracker**
=============================================

**Overview**
---------------

This repository provides a Python script to track the current Large Language Model (LLM) utilization using the IONOS Billing API. The script retrieves the utilization data from the API, processes it, and outputs the results in a JSON format.

**Prerequisites**
-----------------

* IONOS access token (replace `YOUR_ACCESS_TOKEN` in the script)
* IONOS contract ID (replace `YOUR_CONTRACT_ID` in the script)
* Python 3.6+
* `requests` and `json` libraries (included in Python standard library)

**Usage**
---------

1. Clone the repository: `git clone https://github.com/carforge/IONOS_AI_Usage.git`
2. Replace `YOUR_ACCESS_TOKEN` and `YOUR_CONTRACT_ID` in the `IONOS_Billing_API.py` script with your actual credentials.
3. Run the script: `python IONOS_Billing_API.py`

**Output**
----------

The script will output a JSON object containing the current LLM utilization data, including the model name, input, and output quantities.

Example output:
```json
{
    "_SOME-METER-ID_": {
        "mdl_name": "Llama 3.1 405B",
        "input": 111.0,
        "output": 111.0
    },
    "_SOME-METER-ID_": {
        "mdl_name": "Mixtral 8x7B Instruct",
        "input": 111.0,
        "output": 111.0
    }
}

```
**Contributing**
------------

Feel free to contribute to this repository by submitting pull requests or reporting issues.

**License**
-------

This repository is licensed under the MIT License.

**Acknowledgments**
---------------

* IONOS for providing the Billing API
* The developers of the `requests` and `json` libraries

**Disclaimer**
-------------

This script is provided as-is and without warranty. Use at your own risk.