# socket tests
require 'socket'

#socket = Socket.new(:INET, :STREAM)
#addr = Socket.pack_sockaddr_in(4481, '0.0.0.0')
#socket.bind(addr)
#socket.listen(5)

ONE_KB = 1024  # bytes

print 'Max connections: '
p Socket::SOMAXCONN

Socket.tcp_server_loop(4481) do |connection|
    print 'Class: '
    p connection.class
    print 'Fileno: '
    p connection.fileno
    print 'Local addr: '
    p connection.local_address
    print 'Remote addr: '
    p connection.remote_address

    begin
        while data = connection.readpartial(ONE_KB) do
            puts data
        end
    rescue EOFError
        print 'EOF!'
    end

    connection.close
end
