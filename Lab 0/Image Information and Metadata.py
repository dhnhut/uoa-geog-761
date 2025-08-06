if 'google.colab' in str(get_ipython()):
    from google.colab import userdata
    EE_PROJECT_ID = userdata.get('EE_PROJECT_ID') 
else:
    from dotenv import load_dotenv
    import os
    load_dotenv()  # take environment variables
    EE_PROJECT_ID = os.getenv('EE_PROJECT_ID')
    
# Set up GEE API
import ee
ee.Authenticate()
ee.Initialize(project=EE_PROJECT_ID)

# Import other libs
import geemap
