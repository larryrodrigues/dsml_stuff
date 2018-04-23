import sys
import os
import re
import csv
import decimal


def read_knn_test_file(file_to_read=None):
    if os.path.exists(os.path.dirname(file_to_read)):
        tp_count = 0  # True positive
        fp_count = 0  # False Positive
        tn_count = 0  # True Negative
        fn_count = 0  # False Negative
        try:
            with open(file_to_read, 'rb') as csvfile:
                line_num = 0
                datareader = csv.reader(csvfile, delimiter=',')
                for line in datareader:
                    print "{}".format(line)
                    if line_num >= 0:
                        try:
                            customer_id = line[0]
                            num_days    = line[1]
                            account_type = line[2]
                            bank_name = line[3]
                            employment_status = line[4]
                            num_01 = line[5]
                            num_03 = line[6]
                            actual_gb_value = line[12]
                            derrived_gb_value  = line[13]

                            if derrived_gb_value == "Good":
                                if actual_gb_value == "Good":
                                    tp_count = tp_count + 1
                                elif actual_gb_value == "Bad":
                                    fp_count = fp_count + 1
                                else:
                                    print "ERROR: Derrived Good line {}".format(line_num)
                            elif derrived_gb_value == "Bad":
                                if actual_gb_value == "Good":
                                    fn_count = fn_count + 1
                                elif actual_gb_value == "Bad":
                                    tn_count = tn_count + 1
                                else:
                                    print "ERROR: Derrived Bad  line {}".format(line_num)

                        except:
                            print "ERROR could read test data: {}".format(line)
                            e = sys.exc_info()[0]
                            print "Error: {}".format(e)
                            raise
                    line_num = line_num + 1

            print "True Positive: {}".format(tp_count)
            print "False Positive: {}".format(fp_count)
            print "True Negative: {}".format(tn_count)
            print "False Negative: {}".format(fn_count)

            # Accuracy
            accuracy_val = float((tp_count + tn_count))/(tp_count + tn_count+fp_count+fn_count)
            print "Accuracy: {}".format(accuracy_val)
            # [math]Precision(P) = TP / (TP + FP)[/math]
            prec_val = float(tp_count) / (tp_count + fp_count)
            print "Precision: {}".format(prec_val)
            # [math]Recall (R) = TP / (TP + FN) [/math]
            recall_val = float(tp_count) / (tp_count + fn_count)
            print "Recall: {}".format(recall_val)
            # [math] F = 1/((a)(1/P) + (1-a)(1/R))[\math] (WEIGHTED)
            # [math] F = 2PR/(P+R) [\math] (BALANCED)
            f_measure = 2*(prec_val*recall_val)/(prec_val + recall_val)
            print "F-Measure: {}".format(f_measure)
        except:
            print "ERROR could not open file to read: {}".format(file_to_read)
            raise
        finally:
            print "Complete."


def main_withargs(file_in=None):
    print "File in: {}".format(file_in)

    if not file_in == None:
        read_knn_test_file(file_in)


def main_noargs():
    read_knn_test_file(file_to_read="c:/mason/CS-584/HW3/Data_HW3_In_Prog/TestKNN_GoodBad.csv")

    print "Reading Data Complete"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main_withargs(sys.argv[1:])
    else:
        main_noargs()
        print "No args"

print "End Process"