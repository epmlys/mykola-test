# socket client

require 'socket'

#socket = Socket.new(:INET, :STREAM)
#
#remote_addr = Socket.pack_sockaddr_in(80, 'google.com')
#socket.connect(remote_addr)
# ruby way
#socket = TCPSocket.new('google.com', 80)
# another ruby way
#Socket.tcp('google.com', 80) do |connection|
#    connection.write "GET / HTTP/1.1\r\n"
#    connection.close
#end

# without block
#client = Socket.tcp('google.com', 80)

# write to local server
#client = TCPSocket.new('localhost', 4481)
#payload = 'Kolka is cool!' * 10000
#
#begin
#    loop do
#        written = client.write_nonblock(payload)
#        break if written >= payload.size
#        payload.slice!(0, written)
#        IO.select(nil, [client])
#    end

#rescue Errno::EAGAIN
#    IO.select(nil, [client])
#    retry
#end
#client.close

module CloudHash
    class Client
        def initialize(host, port)
            @connection = TCPSocket.new(host, port)
        end

        def get(key)
            request "GET #{key}"
        end

        def set(key, value)
            request "SET #{key} #{value}"
        end

        def request(string)
            msg_length = string.size
            packed_msg_length = [msg_length].pack('i')

            @connection.write(packed_msg_length)
            @connection.write(string)
        end
    end
end

# CloudHash::Client.host = 'localhost'
# CloudHash::Client.port = 4481

# puts CloudHash::Client.set('prez', 'Trumph')
# puts CloudHash::Client.get('prez')
# puts CloudHash::Client.get('vp')
# puts CloudHash::Client.set('kolka', 'Cool!')
# puts CloudHash::Client.get('kolka')

client = CloudHash::Client.new('localhost', 4481)
client.set('prez', 'Trumph')
client.get('prez')
#client.request('exit')
