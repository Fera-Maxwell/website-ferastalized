from livereload import Server, shell

server = Server()
server.watch('index.html')
server.watch('style.css')
server.watch('script.js')
server.watch('test/index.html')
server.watch('test/style.css')
server.watch('test/script.css')
server.serve(root='.', host='0.0.0.0', port=5500)
