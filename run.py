from app import create_app 



#for development
app = create_app('development')

if __name__ == '__main__':
    app.run()
