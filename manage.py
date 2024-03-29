from app import rema_app, db
from flask_script import Manager, Server
from app.models import User, Pitch, Category, Tora, Words
from flask_migrate import Migrate, MigrateCommand

app = rema_app('production')

# app = rema_app('test')development 

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch, Category = Category, Tora = Tora, Words = Words)



if __name__ == '__main__':
    manager.run()