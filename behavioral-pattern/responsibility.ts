/* 
* The Handler interface declares a method for buiding the chain od handless.
* It also declares a method for excuting a request. 
*/

interface Handler {
    setNext(handler: Handler): Handler;
    handle(request: string): string | null;
}
/*
The default chaining behavior can be implemented inside a base handler class. 
*/

abstract class AbstractHandler implements Handler {
    private nextHandler!: Handler;

    public setNext(handler: Handler): Handler {
        this.nextHandler = handler;
        // Returning a handler from here will let us link handless in a
        // convenient way like this:
        // monkey.setNext(squirrel).setNext(dog);
        return handler;
    }

    public handle(request: string): string | null {
        if (this.nextHandler) {
            return this.nextHandler.handle(request)
        }
        return null;
    }

}

/*
All Concrete Handlers either handle a request or pass it to the next handler
in the chain
*/

class MonkeyHandler extends AbstractHandler {
    public handle(request: string): string | null {
        if (request == "Banana") {
            return `Monkey: I'll eat the ${request}`
        }
        return super.handle(request)
    }
}
class SquirrelHandler extends AbstractHandler {
    public handle(request: string): string | null {
        if (request == "Nut") {
            return `Squirrel: I'll eat the ${request}`
        }
        return super.handle(request)
    }
}

class DogHandler extends AbstractHandler {
    public handle(request: string): string | null {
        if (request == "MeatBall") {
            return `Dog: I'll eat the ${request}`
        }
        return super.handle(request)
    }
}

/* Then client code is usually suited to work with single handler. In most
case , it is not even aware that the handler is part of a chain
 */
function clientCode(handler: Handler) {
    const foods = ["Nut", "Banana", "Cup of coffee"];
    for (const food of foods) {
        console.log(`Client: who wants a ${food}`)
        const result = handler.handle(food);
        if (result) {
            console.log(`${result}`)
        } else {
            console.log(`${food} was left untouched`);
        }
    }
}



const monkey = new MonkeyHandler();
const squirrel = new SquirrelHandler();
const dog = new DogHandler();

monkey.setNext(squirrel).setNext(dog);

/* The client should be able to send a request to any handler, not just the 
first one in the chain
 */

console.log("Chain: monkey -> squirrel -> dog\n")
clientCode(monkey);
console.log("");

console.log("Subchain: Squirrel > Dog\n");
clientCode(squirrel);

