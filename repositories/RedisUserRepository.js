const UserRepository = require("./UserRepository");

class RedisUserRepository extends UserRepository {
  constructor(redisClient) {
    super();
    this.redis = redisClient;
  }

  async save(user) {
    const key = `user:${user.id}`;
    await this.redis.set(key, JSON.stringify(user));
  }

  async findById(id) {
    const key = `user:${id}`;
    const data = await this.redis.get(key);

    if (!data) return null;
    return JSON.parse(data);
  }
}

module.exports = RedisUserRepository;