# socket tests
require 'socket'

#socket = Socket.new(:INET, :STREAM)
#addr = Socket.pack_sockaddr_in(4481, '0.0.0.0')
#socket.bind(addr)
#socket.listen(5)

ONE_KB = 1024  # bytes

print 'Max connections: '
p Socket::SOMAXCONN

#Socket.tcp_server_loop(4481) do |connection|
#    print 'Class: '
#    p connection.class
#    print 'Fileno: '
#    p connection.fileno
#    print 'Local addr: '
#    p connection.local_address
#    print 'Remote addr: '
#    p connection.remote_address
#
#    loop do
#        begin
#            data = connection.read_nonblock(ONE_KB)
#            puts data
#        rescue Errno::EAGAIN
#            p IO.select([connection])
#            retry
#        rescue EOFError
#            print 'EOF!'
#            break
#        end
#    end
#    connection.close
#end

SIZE_OF_INT = [11].pack('i').size

# Cloud Hash server
module CloudHash
    class Server
        def initialize(port)
            @server = TCPServer.new(port)
            puts "Listening on port #{@server.local_address.ip_port}"
            @storage = {}
        end

        def start
            Socket.accept_loop(@server) do |connection|
                handle(connection)
                connection.close
            end
        end

        def handle(connection)
            packed_msg_length = connection.read(SIZE_OF_INT)
            msg_length = packed_msg_length.unpack('i').first

            request = connection.read(msg_length)
            # write back result of processing
            connection.write(process(request))
        end

        # SET key, GET key
        def process(request)
            command, key, value = request.split
            case command.upcase
            when 'GET'
                @storage[key]
            when 'SET'
                @storage[key] = value
                "Has Inserted #{key} - #{value}"
            end
        end
    end
end

server = CloudHash::Server.new(4481)
server.start
