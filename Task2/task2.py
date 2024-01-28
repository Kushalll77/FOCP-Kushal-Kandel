import sys
#written  to handle the reading of the log file
def analyze_log(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found - {log_file_path}")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

# Variables for analysis
    correct_entry = 0
    doused_cats = 0
    total_time_inside = 0
    correct_visits = []
   
    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        if len(parts) == 3:
            cat_name, entry_time, dept = parts
            entry_time = int(entry_time)
            dept = int(dept)

            if cat_name == 'OURS':
                correct_entry += 1
                time_inside = dept - entry_time
                total_time_inside += time_inside
                correct_visits.append(time_inside)
            else:
                doused_cats += 1

    if correct_entry == 0:
        print("No data found")
    else:
        total_hours=total_time_inside/60
        average = sum(correct_visits) / correct_entry
        maximum = max(correct_visits)
        minimum = min(correct_visits)
       
        print("Log File Analysis")
        print("=================")
        print("Total number of times the correct cat has entered the house is:",correct_entry)
        print("Number of times cats were doused with water:",doused_cats)
        print("Total time spent in the house by the correct cat: {:.2f} hours".format(total_hours))
        print("Average duration of each visit by the correct cat: {:.2f} minutes".format(average))
        print("Duration of the longest visit by the correct cat:",maximum,"minutes")
        print("Duration of the shortest visit by the correct cat:",minimum,"minutes")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    analyze_log(log_file_path)

