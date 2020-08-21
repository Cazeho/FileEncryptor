import logging

# create logger




file= "info.pdf"
logging.basicConfig(filename="custom_log_output.log",filemode="a",format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Encrypt' + " - " + file)


with open("custom_log_output.log" , 'r') as f:
    for line in f:
        print(line)
	#"\n"


