import io
import pandas as pd

def clean_csv(input_stream):
    """
    :param input_stream: (StringIO) An in-memory stream for text I/O containing CSV data
    :returns: (String) A string containing CSV data
    """
    df = pd.read_csv(input_stream)
    return df.dropna().to_csv(index=False, header=False)

input_stream = io.StringIO("Name,Surname\nJohn,Doe\nAnn,Franklin")
result_csv = clean_csv(input_stream)

print(result_csv)
input_stream.close()