const redisClient = require("./infrastructure/redisClient");
const RedisUserRepository = require("./repositories/RedisUserRepository");
const UserService = require("./services/UserService");

async function main() {
  const userRepository = new RedisUserRepository(redisClient);

  const userService = new UserService(userRepository);

  const user = await userService.registerUser({
    name: "Darth Vader",
    email: "dv@empire.org"
  });

  console.log("Saved user:", user);

  const foundUser = await userService.getUser(user.id);

  console.log("Loaded user:", foundUser);
}

main();