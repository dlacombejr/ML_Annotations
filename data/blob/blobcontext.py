from azure.storage.blob import BlockBlobService

def get_conn():
    bbs = BlockBlobService(account_name='ACCOUNT NAME',
                           account_key='ACCOUNT KEY')
    return bbs

def save_blob(blob_name, value):
    bbs = get_conn()
    bbs.create_container('annotations')
    bbs.create_blob_from_text('annotations', blob_name + '.csv', value)
