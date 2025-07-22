import logging 

logging.basicConfig( filename= 'error.log',level=logging.DEBUG, format= '%(asctime)s - %(levelname)s- %(message)s')


class Heighttoolow(Exception):
    pass

def check_ing(height):
    if height <= 165 :
        raise Heighttoolow("Must be greater than 165 cm")
    else : 
        print("Height is ok")

try :
    check_ing(155)
except Exception as e :
    print("Error",e)
    logging.error(f"Caught HEightTooLow error {e}")
finally :
    print("This runs no matter what")