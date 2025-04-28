import numpy as np
import requests
import json
import datetime

with open("secrets.json") as json_file:
    secrets = json.load(json_file)
apikey = secrets['api_key']

def currency_conversions():
    currencies_dict = {}
    req = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&currencies=USD%2CSEK&base_currency=GBP")
    data = json.loads(req.content)['data']
    gbp_dict ={'GBP': 1,
           'SEK': data['SEK'],
           'USD': data['USD']}
    currencies_dict['GBP'] = gbp_dict
    req = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&currencies=GBP%2CUSD&base_currency=SEK")
    data = json.loads(req.content)['data']
    sek_dict ={'SEK': 1,
           'GBP': data['GBP'],
           'USD': data['USD']}
    currencies_dict['SEK'] = sek_dict
    return currencies_dict 
conversions = currency_conversions()

def convert_currencies(amount_in, currency_in, currencies_out):
    amounts = {}
    for currency in currencies_out:
        amounts[currency] = amount_in * conversions[currency_in][currency]
    return amounts

def format_amounts(amounts, sig_fig):
    format_str=""
    for key, val in amounts.items():
        if key=='GBP':
            format_str += '£' + format(int(np.round(val,-sig_fig)), ",") + '/'
        elif key=='USD':
            format_str += '$' + format(int(np.round(val,-sig_fig)), ",") + '/'
        elif key=='SEK':
            format_str += format(int(np.round(val,-sig_fig-1)), ",").replace(",", " ") + 'SEK' '/'            
    return format_str[:-1]

def convert_str(raw_str):
    _, amount_in, currency_in, currencies_out = raw_str.split(';')
    amount_in = int(amount_in)
    currencies_out = currencies_out[1:-1].split(",")
    sig_fig = max(len(str(amount_in))-3, 1)
    converted_amounts = convert_currencies(amount_in, currency_in, currencies_out)
    out_str = format_amounts(converted_amounts, sig_fig)
    return out_str


def main():
    with open("content/pages/pay_raw.md", "r") as infile:
        with open("content/pages/pay.md", "w") as outfile:
            for line in infile.readlines():
                if line == 'Status: draft\n':
                    continue
                parts = line.split("**")
                for i, part in enumerate(parts):
                    if len(part) == 0:
                        continue
                    if part[:4]=="CONV":
                        parts[i] = convert_str(part)
                new_line = "**".join(parts)
                outfile.write(new_line)
            outfile.write(f" Currency conversion performed on {str(datetime.datetime.now())[:11]}.")


if __name__ == "__main__":
    main()
