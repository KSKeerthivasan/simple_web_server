from http.server import HTTPServer,BaseHTTPRequestHandler
content ="""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Laptop Configuration</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f1f8ff; /* Light blue background for the page */
      color: #333;
    }
    .container {
      max-width: 900px;
      margin: 50px auto;
      background: #ffffff; /* White background for the container */
      padding: 30px;
      border-radius: 16px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      font-size: 32px;
      color: #ff6347; /* Tomato color for the title */
      margin-bottom: 20px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      background: #f4f4f9; /* Light gray background for the table */
    }
    th, td {
      padding: 16px 20px;
      text-align: left;
      border: 1px solid #ddd;
    }
    th {
      background-color: #4CAF50; /* Green color for the table header */
      color: white;
      font-weight: bold;
      text-transform: uppercase;
    }
    td {
      background-color: #ffffff; /* White background for table data cells */
      color: #555;
    }
    tr:nth-child(even) td {
      background-color: #f9f9f9; /* Light gray for even rows */
    }
    tr:hover td {
      background-color: #e0f7fa; /* Light cyan for hovered rows */
      color: #00796b; /* Dark teal text on hover */
    }
    td:first-child {
      font-weight: bold;
      color: #00796b; /* Dark teal color for the configuration column */
    }
    td:last-child {
      font-style: italic;
      color: #666;
    }
    .highlight {
      background-color: #fff9c4; /* Pale yellow background for highlighted rows */
      font-weight: bold;
    }
    @media (max-width: 768px) {
      .container {
        padding: 20px;
      }
      table {
        font-size: 14px;
      }
      th, td {
        padding: 10px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Laptop Configuration</h1>
    <table>
      <tr>
        <th>Configuration</th>
        <th>Details</th>
      </tr>
      <tr>
        <td class="highlight">Operating System</td>
        <td>Windows 11 Home Single Language 64-bit</td>
      </tr>
      <tr>
        <td>Processor</td>
        <td>13th Gen Intel(R) Core(TM) i5-13450HX (16 CPUs)</td>
      </tr>
      <tr>
        <td class="highlight">RAM</td>
        <td>16 GB</td>
      </tr>
      <tr>
        <td>Storage</td>
        <td>1 TB SSD</td>
      </tr>
      <tr>
        <td class="highlight">Graphics Card</td>
        <td>NVIDIA GeForce RTX 3050 (6GB)</td>
      </tr>
      <tr>
        <td>Screen Resolution</td>
        <td>1920 x 1080 (Full HD)</td>
      </tr>
      <tr>
        <td class="highlight">Screen Size</td>
        <td>15.6 inches</td>
      </tr>
      <tr>
        <td>Battery Capacity</td>
        <td>56 WHr</td>
      </tr>
      <tr>
        <td class="highlight">Weight</td>
        <td>2.8 kg</td>
      </tr>
      <tr>
        <td>Color</td>
        <td>Matt Black</td>
      </tr>
      <tr>
        <td class="highlight">Keyboard</td>
        <td>Orange-Backlit, QWERTY</td>
      </tr>
      <tr>
        <td>Wireless Connectivity</td>
        <td>Wi-Fi 6, Bluetooth 5.3</td>
      </tr>
      <tr>
        <td class="highlight">Ports</td>
        <td>USB-C, USB-A, HDMI, Ethernet</td>
      </tr>
      <tr>
        <td>Operating System Architecture</td>
        <td>64-bit</td>
      </tr>
    </table>
  </div>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):  
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address =('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()