import csv
from fpdf import FPDF 

# Define the name of our data file
file_name = 'website_traffic.csv'
data = []

# Reading the data from the given CSV file 
with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert views and duration to numbers so we can do math
        row['Views'] = int(row['Views'])
        row['Duration'] = float(row['Duration'])
        data.append(row)

# Analysis of the data 

total_views = sum(row['Views'] for row in data) # Calculating Total Page Views

total_duration = sum(row['Duration'] for row in data) # Calculating Average Visit Duration
average_duration = total_duration / len(data)

# Find Most Popular Pages -- Here We'll group views by page

page_views = {}
for row in data:
    page = row['Page']
    views = row['Views']
    page_views[page] = page_views.get(page, 0) + views

# Sort the pages by views in descending order
sorted_pages = sorted(page_views.items(), key=lambda item: item[1], reverse=True)

# 4. Find Top Locations
# We'll group views by location
location_views = {}
for row in data:
    location = row['Location']
    views = row['Views']
    location_views[location] = location_views.get(location, 0) + views

# Sort the locations by views in descending order
sorted_locations = sorted(location_views.items(), key=lambda item: item[1], reverse=True)

# Let's print the results of our analysis to check them
print("\n--- Analysis Results ---")
print(f"Total Page Views: {total_views:,}") # The :, adds commas for readability
print(f"Average Visit Duration: {average_duration:.2f} minutes") # .2f formats to two decimal places
print("\nPage Views by Page:")
for page, views in sorted_pages:
    print(f"- {page}: {views:,} views")
print("\nPage Views by Location:")
for location, views in sorted_locations:
    print(f"- {location}: {views:,} views")

# --- GENERATING THE PDF REPORT  ---

# Set up the PDF document
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)

# Add a title to the report
pdf.cell(200, 10, txt="Website Traffic Analysis Report", ln=True, align="C")
pdf.set_font("Arial", size=12)
pdf.cell(200, 5, txt="(Data from website_traffic.csv)", ln=True, align="C")

# Add a section for key metrics
pdf.ln(10)
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Key Metrics", ln=True)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Total Page Views: {total_views:,}", ln=True)
pdf.cell(200, 10, txt=f"Average Visit Duration: {average_duration:.2f} minutes", ln=True)

# Add a section for popular pages
pdf.ln(5)
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Most Popular Pages", ln=True)

pdf.set_font("Arial", size=12)
for page, views in sorted_pages:
    pdf.cell(200, 8, txt=f"- {page}: {views:,} views", ln=True)

# Add a section for top locations
pdf.ln(5)
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Top Locations", ln=True)

pdf.set_font("Arial", size=12)
for location, views in sorted_locations:
    pdf.cell(200, 8, txt=f"- {location}: {views:,} views", ln=True)

# Save the PDF to a file
output_file = "website_traffic_report.pdf"
pdf.output(output_file)

print(f"\nReport successfully generated and saved as '{output_file}'!")