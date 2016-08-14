#!/usr/bin/env python

import pickle
import sys
import os
import collections
import csv
import pandas as pd

def print_usage(argv):
    print "Usage: %s <indir>"%(argv[0])
    print "    where indir is the directory containing the moral dilemma task psydat files to be parsed"
    print "    if blank this is assumed to be the current directory"


def parse_morald_data_file( filename, standard_scores ):
    
    # dictionary of values used to standardize scores
    n_blocks = 8
    n_items = 6
    
    # variables to calculate average response times and quality of response
    control_times = 0.0
    control_resp = 0.0
    dilemma_times = 0.0
    dilemma_resp = 0.0
    
    responses = []
    
    # identifier that we will use in the output tables for this file
    file_key=(filename.split('/')[-1]).split(".")[0]
        
    # load in the file as a pandas dataframe, which should simplify processing
    try:
        psydata=pd.read_csv(filename)
    except AttributeError:
        pass
    except Exception, e:
        print "Could not open pickle file %s (%s)"%(filename, repr(e))
        raise
        
    # perform basic checks to ensure that we are dealing with a moral dilemma
    # logfile
    if 'dilemma_image' not in psydata.columns or 'dilemma_sound' not in psydata.columns or \
       'control_image' not in psydata.columns or 'control_sound' not in psydata.columns:
        print psydata.keys()
        print sys.version
        print "%s does not appear to be a moral dilemma logfile"%(filename)
        raise AttributeError 

    
    if len(psydata) != 48:
        print "%s does not contain enough entries for moral dilemma data: %d (48)"%(filename, len(psydata))
        raise AttributeError
        
    for block in range(0,n_blocks):
        for item in range(0,n_items):
            # get the index of the next value
            ndx=block*n_items+item
            
            #even number blocks are control and odd number blocks are dilemmas
            if block % 2 == 0:
                
                # the stimuli are randomized, so get the name of this response
                control_stim = psydata['control_image'][ndx].split('/')[-1].split(".")[0]
                #control_stim = psydata.entries[ndx]['control_image'].split('/')[-1].split(".")[0]
                
                # make sure that there was a response
                if psydata['key_resp_3.rt'][ndx] and psydata['key_resp_3.keys'][ndx] != 'None':
                    
                    # compute the reaction time as the time from the end of the audio question,
                    # this might result in negative reaction times, but it allows us to control
                    # for the difference in question length between control and dilemma trials
                    control_times+=psydata['key_resp_3.rt'][ndx]-standard_scores[control_stim][0]
                    #control_times+=psydata.entries[ndx]['key_resp_3.rt']-standard_scores[control_stim][0]
                    
                    # keep track of whether the response was correct or not
                    control_resp+=standard_scores[control_stim][int(psydata['key_resp_3.keys'][ndx])]
                    #control_resp+=standard_scores[control_stim][int(psydata.entries[ndx]['key_resp_3.keys'])]
                    
                    # store an entry that will go in a dataframe for a more intensive analysis
                    responses.append([file_key, control_stim,
                        psydata['key_resp_3.rt'][ndx]-standard_scores[control_stim][0],
                        standard_scores[control_stim][int(psydata['key_resp_3.keys'][ndx])]])
                    #responses.append([file_key, control_stim,
                    #    psydata.entries[ndx]['key_resp_3.rt']-standard_scores[control_stim][0],
                    #    standard_scores[control_stim][int(psydata.entries[ndx]['key_resp_3.keys'])]])
                else:
                    
                    # record that there was no response to the stimulus
                    responses.append([file_key, control_stim, None, None])
                        
            elif block % 2 == 1:
                
                # get the name of this stimuli
                dilemma_stim = psydata['dilemma_image'][ndx].split('/')[-1].split(".")[0]
                #dilemma_stim = psydata.entries[ndx]['dilemma_image'].split('/')[-1].split(".")[0]
                
                # make sure that there was a response
                if psydata['key_resp_4.rt'][ndx] and psydata['key_resp_4.keys'][ndx] != 'None':

                    # calculate the reaction time from the end of the audio prompt, this may result in 
                    # negative response times, but allows us to control for the different in length between
                    # the control and dilemma audio prompts
                    dilemma_times+=psydata['key_resp_4.rt'][ndx]-standard_scores[dilemma_stim][0]
                    #dilemma_times+=psydata.entries[ndx]['key_resp_4.rt']-standard_scores[dilemma_stim][0]
                    
                    # calculate the fraction of the normative sample that answered the dilemma similarily
                    dilemma_resp+=standard_scores[dilemma_stim][int(psydata['key_resp_4.keys'][ndx])]
                    #dilemma_resp+=standard_scores[dilemma_stim][int(psydata.entries[ndx]['key_resp_4.keys'])]
                    
                    # store an entry in the data frame
                    responses.append([file_key,dilemma_stim,psydata['key_resp_4.rt'][ndx]-standard_scores[dilemma_stim][0],
                        standard_scores[dilemma_stim][int(psydata['key_resp_4.keys'][ndx])]])
                    #responses.append([file_key,dilemma_stim,psydata.entries[ndx]['key_resp_4.rt']-standard_scores[dilemma_stim][0],
                    #    standard_scores[dilemma_stim][int(psydata.entries[ndx]['key_resp_4.keys'])]])
                        
                else:
                    
                    # record that there was no response to the stimulus
                    responses.append([file_key, dilemma_stim, None, None])
                        
    return((control_times/24,control_resp/24,dilemma_times/24,dilemma_resp/24,responses))            
   
def main(argc,argv):
    
    # we require the name of the directory to run, if not found, lets assume that the user doesn't know
    # how to run the program correctly and print the usage
    if argc != 2:
        print_usage(argv)
        sys.exit(1)
    # the only parameter we take is the path to the folder containing the psydat files, lets
    # make sure that it is legit
    elif os.path.isdir(argv[1]):
        indir = argv[1]
    # the path may be to a subdirectory in the current working directory, lets try that
    elif os.path.isdir(os.path.join(os.getcwd(),argv[1])):
        indir = os.path.join(os.getcwd(),argv[1])
    else:
        print_usage(argv)
        print "ERROR: %s and %s are not a valid directories"%(argv[1],os.path.join(os.getcwd(),argv[1]))
        sys.exit(1)
        
    # read in the standardized values
    standard_scores=collections.defaultdict()

    
    with open("morald_qtimes.txt") as fd:
        for line in fd.readlines():
            line=line.strip().split(",")
            key=unicode(line[0])
            vals=[float(v) for v in line[2:]]
            standard_scores[key]=vals
    print standard_scores
    
    # get all of the files in the input directory
    datfiles=[ os.path.join(indir,f) for f in os.listdir(indir) if os.path.isfile(os.path.join(indir,f)) and f.endswith(".csv") ]    
    
    # if there are no files in the directory, tell the user to try again
    if len(datfiles) < 1:
        print_usage(argv)
        print "ERROR: %s does not contain any files that end in .psydat"%(indir)
        sys.exit(1)
        
    # otherwise let the user know that we are good to go
    print "---"
    print "Running %s on the %d moral dilemma task"%(argv[0], len(datfiles))
    print "psydat files in %s"%(indir)
    print "---"
    
    group_stats=[]
    dframe=[]
    
    except_count=0
    for file in datfiles:
        print "parsing %s"%(file)
        try:
            (control_times,control_resp,dilemma_times,dilemma_resp,responses)=parse_morald_data_file(file,standard_scores)
        except Exception, e:
            except_count+=1
            print "exception %d %s"%(except_count, repr(e))
            continue
        file_key=(file.split("/")[-1]).split(".")[0]
        group_stats.append([file_key,control_times,control_resp,dilemma_times,dilemma_resp])
        dframe.extend(responses)

    print "retrived %d statistics"%(len(group_stats))
    
    with open("morald_group_stats_cc.csv","w") as ofd:
        outwriter=csv.writer(ofd)
        outwriter.writerow(["file","control rt","control resp","dilemma rt","dilemma resp"])
        outwriter.writerows(group_stats)
  
    with open("morald_dframe_cc.csv","w") as ofd:
        outwriter=csv.writer(ofd)
        outwriter.writerow(["file","condition","resp","rt"])
        outwriter.writerows(dframe)
                        
#    print(group_stats)
#    print(dframe)


if __name__ == "__main__":

    main(len(sys.argv),sys.argv)