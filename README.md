1. Install --> Python 3.10. -> Postgresql -> pgAdmin -> Pycharm.
6. Create venv of python. (python3.10 -m venv odoo-venv)
7. Activate virtual enviornment: (odoo-venv\Scripts\activate)
8. Install all required files by odoo in odoo-18.0/requiremnets.txt with command: (pip install -r requirements.txt)
9. Configure in PyCharm as "Add the Interpreter for Odoo"
  10. Add the odoo-18.0/odoo-bin file as script with -c path/of/conf/file
11. Then run the code and create the db
