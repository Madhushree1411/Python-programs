from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #ff6a00, #ee0979);
            margin: 0;
            padding: 0;
        }

        .container{
            width: 420px;
            margin: 60px auto;
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
        }

        h1{
            text-align: center;
            color: #ee0979;
        }

        label{
            font-weight: bold;
        }

        input, select{
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        button{
            width: 100%;
            padding: 12px;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
        }

        button:hover{
            opacity: 0.9;
        }

        .result{
            margin-top: 20px;
            background: #f3f3f3;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
        }

        .error{
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Calculator</h1>

    <form method="POST">
        <label>First Number</label>
        <input type="number" step="any" name="num1" required>

        <label>Second Number</label>
        <input type="number" step="any" name="num2" required>

        <label>Operation</label>
        <select name="op">
            <option value="add">Addition (+)</option>
            <option value="sub">Subtraction (-)</option>
            <option value="mul">Multiplication (*)</option>
            <option value="div">Division (/)</option>
        </select>

        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
    <div class="result">
        <h3>Result</h3>
        <p>{{result}}</p>
    </div>
    {% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["op"]

        if op == "add":
            result = num1 + num2
        elif op == "sub":
            result = num1 - num2
        elif op == "mul":
            result = num1 * num2
        elif op == "div":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero"

    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
