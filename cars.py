#!/usr/bin/env python3

import json
import locale
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import emails

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    max_revenue = {"revenue": 0}
    max_sales = {"sales": 0, "car": None}
    car_year_count = {}

    for item in data:
        item_sales = item["total_sales"]
        car_year = item["car"]["car_year"]
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item_price * item_sales

        if item_revenue > max_revenue["revenue"]:
            max_revenue["revenue"] = item_revenue
            max_revenue["car"] = item["car"]

        if item_sales > max_sales["sales"]:
            max_sales["sales"] = item_sales
            max_sales["car"] = item["car"]

        car_year_count[car_year] = car_year_count.get(car_year, 0) + 1

    most_popular_car_year = max(car_year_count, key=car_year_count.get)
    most_popular_car_count = car_year_count[most_popular_car_year]

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]
        ),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["sales"]
        ),
        "The most popular year was {} with {} sales".format(
            most_popular_car_year, most_popular_car_count
        ),
    ]

    return summary



def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def generate_report(filename, summary, table_data):
    """Generates a PDF report with the given summary and table data."""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create report content
    report = []
    report.append(Paragraph("Car Sales Summary", styles["Heading1"]))
    report.append(Paragraph(summary[0], styles["Normal"]))
    report.append(Paragraph(summary[1], styles["Normal"]))
    report.append(Paragraph(summary[2], styles["Normal"]))

    # Create and style the table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    report.append(table)

    # Build the PDF document
    doc.build(report)

def send_email(sender_email, receiver_email, subject, body, attachment_path):
    message = emails.Message(
        subject=subject,
        mail_from=sender_email,
        text=body,
        attachments=[{"filename": "cars.pdf", "path": attachment_path}],
    )
    message.send(to=receiver_email, smtp={"host": "localhost", "port": 25})
    return True  # Assume email is sent successfully


def main(argv):
    data = load_data("car_sales.json")
    summary = process_data(data)
    table_data = cars_dict_to_table(data)

    # Generate the PDF report and save it to "/tmp/cars.pdf"
    generate_report("/tmp/cars.pdf", summary, table_data)

    sender_email = "automation@example.com"
    receiver_email = "<user>@example.com"  # Replace <user> with the actual user
    subject = "Sales summary for last month"
    body = "\n".join(summary)

    # Send the email with the PDF report attachment
    if send_email(sender_email, receiver_email, subject, body, "/tmp/cars.pdf"):
        print("Email sent with the PDF report attachment.")
    else:
        print("Email failed to send.")


if __name__ == "__main__":
    main(sys.argv)