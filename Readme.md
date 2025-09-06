<body>

  <h3>Steps to Start the Chatbot</h3>

  <p>Follow these step-by-step instructions to set up and start the chatbot project.</p>

  <h4>1. <strong>Set Up the Project Folder Structure</strong></h4>
  <p>Ensure the following folder structure is in place:</p>
  <pre><code>
/chatbot_project
  /static
    index.html  &lt;-- Place your HTML file here
  app.py         &lt;-- Flask server code
  chatbot.py     &lt;-- Optional, backend logic for chatbot
  </code></pre>

  <h4>2. <strong>Install Python and Required Libraries</strong></h4>
  <p>Make sure Python is installed on your system. If not, download it from 
    <a href="https://www.python.org/">python.org</a>.
  </p>
  <p>Next, install Flask by running this command in your terminal or command prompt:</p>
  <pre><code>pip install flask</code></pre>

  <h4>3. <strong>Write the Files</strong></h4>
  <ul>
    <li><strong>app.py</strong>: This file contains the Flask server logic. Copy the following code into your <code>app.py</code> file:</li>
  </ul>
  <pre><code>from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5500)
  </code></pre>

  <ul>
    <li><strong>static/index.html</strong>: This file is your chatbot’s frontend interface. Add your chatbot UI code here.</li>
  </ul>

  <h4>4. <strong>Run the Flask Server</strong></h4>
  <ol>
    <li>Open a terminal or command prompt.</li>
    <li>Navigate to the project directory using:
      <pre><code>cd /path/to/chatbot_project</code></pre>
    </li>
    <li>Start the Flask server by running:
      <pre><code>python app.py</code></pre>
    </li>
    <li>You should see output like:
      <pre><code>Running on http://127.0.0.1:5500/</code></pre>
    </li>
  </ol>

  <h4>5. <strong>Access the Chatbot in a Browser</strong></h4>
  <ul>
    <li>Open your web browser.</li>
    <li>Enter the following URL:
      <pre><code>http://127.0.0.1:5500/</code></pre>
    </li>
    <li>The chatbot interface from <code>index.html</code> should load.</li>
  </ul>

  <h4>6. <strong>Troubleshooting</strong></h4>
  <ul>
    <li>If you encounter a <code>404 Not Found</code> error, ensure:
      <ul>
        <li>The <code>index.html</code> file is inside the <code>/static</code> folder.</li>
        <li>Your <code>app.py</code> file points to the correct static folder.</li>
      </ul>
    </li>
    <li>Restart the Flask server after making any changes to your files.</li>
  </ul>

  <h4>7. <strong>Optional: Modify the Chatbot Logic</strong></h4>
  <p>If you want to add chatbot functionality, write the logic in <code>chatbot.py</code> and integrate it into <code>app.py</code>. For example:</p>
  <pre><code>@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = generate_response(user_message)  # Your chatbot logic here
    return jsonify({"reply": response})
  </code></pre>

  <h4>8. <strong>Stop the Server</strong></h4>
  <ul>
    <li>To stop the Flask server, press <code>Ctrl + C</code> in the terminal.</li>
  </ul>

  <hr>
  <p>By following these steps, you can successfully set up, run, and interact with your chatbot!</p>

</body>
