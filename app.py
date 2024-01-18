from flask import Flask, render_template, request
import requests
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import ttk, simpledialog

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    visualizer = EthereumTransactionVisualizer()
    address = visualizer.get_user_input()
    transactions = visualizer.get_transaction_data(address)
    
    if transactions:
        visualizer.visualize_transaction_path(transactions)
        return "Python code executed successfully"
    else:
        return "No transactions found."

if __name__ == '__main__':
    app.run(debug=True)
