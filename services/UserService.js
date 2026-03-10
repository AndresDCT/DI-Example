const crypto = require("crypto");

class UserService {
  constructor(userRepository) {
    this.userRepository = userRepository;
  }

  async registerUser(userData) {
    const user = {
      id: crypto.randomUUID(),
      name: userData.name,
      email: userData.email
    };

    await this.userRepository.save(user);

    return user;
  }

  async getUser(id) {
    return await this.userRepository.findById(id);
  }
}

module.exports = UserService;