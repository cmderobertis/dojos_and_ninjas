from flask import Flask, render_template, session, request, redirect, url_for
app = Flask(__name__)
app.secret_key = 'I suppose changing this is not absolutely necessary, but do it anyway.'
