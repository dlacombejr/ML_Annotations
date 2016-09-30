import pandas as pd
from data.sql import dbcontext
from data.blob import blobcontext

def save_session_annotations(sess_id, annotations):
    datavals = dbcontext.get_session_data(sess_id)
    for ann in annotations:
        ann['raw_data'] = datavals[(datavals['time'] >= ann['tag_start']) & (datavals['time'] <= ann['tag_end'])]
    dfAnn = pd.DataFrame(annotations)
    value = dfAnn.to_json()
    blobcontext.save_blob(str(sess_id), value)
    return 'success'