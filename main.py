from nicegui import ui

ui.markdown('''
# Helpdesk
This is a simple helpdesk tool.
''')

ui.link('View on GitHub', 'https://github.com/michivonah/helpdesk')
            
ui.button('Load tickets!', on_click=lambda: ui.notify('Please connect to a database!', close_button='OK'))

ui.input(label='Username')

ui.input(label='Password')

ui.button('Sign in')

# Start App
ui.colors(primary='#9b59b6', secondary='#8e44ad', accent='#f1c40f')
ui.run(title='Helpdesk by Michi', dark='false')

