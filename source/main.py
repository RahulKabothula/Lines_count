import util
from read_file import read_file
from transform import number_of_lines, number_of_words
from load import load

def main(file_path,result_path):
    # Creating Spark Session
    spark = util.get_spark_session()

    #Reading text file
    df = read_file(spark, file_path)

    # Transform files
    output = number_of_lines(df)
    output = number_of_words(output, df)

    #Load the output
    load(result_path,output)

if __name__ == '__main__':
    lines_path = "C:\\Users\\Rahul Kabothula\\training\\data_engineering\\projects\\lines_count\\data\\lines.txt"
    sample1_path = "C:\\Users\\Rahul Kabothula\\training\\data_engineering\\projects\\lines_count\\data\\sample1.txt"
    lines_output_path = "C:\\Users\\Rahul Kabothula\\training\\data_engineering\\projects\\lines_count\\result\\linesOutput"
    sample1_output_path = "C:\\Users\\Rahul Kabothula\\training\\data_engineering\\projects\\lines_count\\result\\sample1Output"
    main(lines_path, lines_output_path)
    main(sample1_path, sample1_output_path)


