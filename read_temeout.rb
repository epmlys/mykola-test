require 'socket'
require 'timeout'

TIMEOUT = 5  # seconds

Socket.tcp_server_loop(4481) do |connection|
    begin
        connection.read_nonblock(4096)
    rescue Errno::EAGAIN
        if IO.select([connection], nil, nil, TIMEOUT)
            retry
        else
            raise Timeout::Error
        end
    end
    connection.close()
end
