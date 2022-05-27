from library import Library
import Pyro4

if __name__ == '__main__':

	daemon = Pyro4.Daemon()
	uri = daemon.register(Library)
	ns = Pyro4.locateNS()
	ns.register('library', uri)
	daemon.requestLoop()