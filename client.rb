# socket client

require 'socket'

socket = Socket.new(:INET, :STREAM)

remote_addr = Socket.pack_sockaddr_in(80, 'google.com')
socket.connect(remote_addr)

# ruby way
socket = TCPSocket.new('google.com', 80)

# another ruby way
Socket.tcp('google.com', 80) do |connection|
    connection.write "GET / HTTP/1.1\r\n"
    connection.close
end

# without block
client = Socket.tcp('google.com', 80)

# write to local server
client = TCPSocket.new('localhost', 4481)
client.write('Kolka is cool!')
client.close
