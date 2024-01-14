import multiprocessing

def process_data(data_chunk):
    processed_data = [line.upper() for line in data_chunk]
    return processed_data

def main():
    with open('large_dataset.txt', 'r') as file:
        data = file.readlines()

    num_processes = multiprocessing.cpu_count()

    chunk_size = len(data) // num_processes
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    pool = multiprocessing.Pool(processes=num_processes)


    processed_results = pool.map(process_data, data_chunks)

    pool.close()
    pool.join()

    final_result = []
    for result in processed_results:
        final_result.extend(result)

    with open('output_result.txt', 'w') as output_file:
        output_file.writelines(final_result)

if __name__ == '__main__':
    main()
