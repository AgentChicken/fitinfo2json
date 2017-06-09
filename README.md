# fitinfo2json

fitinfo2json.py is a simple Python script to convert the output of Thomas Robitaille's SEDfitter library into an easily parseable JSON format. To use the script, you'll need to install sedfitter and argparse (os should come with your Python distribution out of the box); both can be installed using `pip install sedfitter argparse`. To run the script, simply pass in the name of the FITINFO file (it's probably output.fitinfo) and the name of your desired output file as parameters, in that order.
