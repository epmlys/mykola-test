require 'socket'
require 'openssl'

socket = TCPSocket.new('0.0.0.0', 4481)

ssl_socket = OpenSSL::SSL::SSLSocket.new(socket)
ssl_socket.connect()
p ssl_socket.read()
