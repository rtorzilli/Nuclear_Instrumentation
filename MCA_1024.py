import pandas as pd
#------------------------------------------------------------------------------#
def MCA_1024(path):
    colNames = ['Counts', 'Channel', 'Energy [keV]']
    df = pd.DataFrame(columns=colNames)
    # Header Lines skips this many lines 
    headerLines = 12
    Header=True 
    Channel=0 # Initialize Channel
    # Create and open input file
    # Loop over the file lines and store data to pandas dataframe. 
    try:
        with open(path, "r") as f:
            for line in f: 
                splitList = line.strip().split()
                if splitList[0].strip() == "$ENER_FIT:":
                    line = f.next() # Skip a line 
                    splitList = line.strip().split()
                    intercept=float(splitList[0].strip())
                    slope=float(splitList[1].strip())
                    # These are used later to ID the channel and Channel Energy
            # Read the output file line by line
                    # Close the file
        with open(path, "r") as f:
            for line in f:
                Channel=Channel+1 # Increment Channel 
                # If end of counts found, consolidate gains
                if Channel<1025:
    #                print splitList[0].strip()
    #                if splitList[0].strip() == "$ROI:":
    #                    return df 
                    splitList = line.strip().split()
                    # Skip header lines
                    if Header==True:
                        for i in range(0, headerLines):
                            line = f.next()
                            Header=False
                            splitList = line.strip().split()
                    Energy=(Channel)*slope+intercept
                    df= df.append(pd.Series([float(splitList[0].strip()),
                           Channel,Energy],index=colNames), ignore_index=True)
            return df 
        # Close the file
        f.close()
        assert f.closed == True, "File ({}) didn't close properly.".format(path)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print "File not found was: {0}".format(path)