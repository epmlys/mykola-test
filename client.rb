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
#client.write('Kolka is cool!')
#client.close

module CloudHash
    class Client
        class << self
            attr_accessor :host, :port
        end

        def self.get(key)
            request "GET #{key}"
        end

        def self.set(key, value)
            request "SET #{key} #{value}"
        end

        def self.request(string)
            # create new connection for each operation
            @client = TCPSocket.new(host, port)
            @client.write(string)

            # send EOF
            @client.close_write

            # get response
            @client.read
        end
    end
end

CloudHash::Client.host = 'localhost'
CloudHash::Client.port = 4481

puts CloudHash::Client.set('prez', 'Trumph')
puts CloudHash::Client.get('prez')
puts CloudHash::Client.get('vp')
puts CloudHash::Client.set('kolka', 'Cool!')
puts CloudHash::Client.get('kolka')

