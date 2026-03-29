// Import necessary modules and types
import { GraphQLObjectType, GraphQLString, GraphQLList } from 'graphql';
import { Order, Customer, Coupon, Review, Governorate, Setting } from './models';

// Define resolvers for the queries
const resolvers = {
  orders: async () => await Order.find(),
  customers: async () => await Customer.find(),
  coupons: async () => await Coupon.find(),
  reviews: async () => await Review.find(),
  governorates: async () => await Governorate.find(),
  settings: async () => await Setting.find(),
};

// Define the GraphQL schema with the resolvers
const Query = new GraphQLObjectType({
  name: 'Query',
  fields: {
    orders: { type: new GraphQLList(OrderType), resolve: resolvers.orders },
    customers: { type: new GraphQLList(CustomerType), resolve: resolvers.customers },
    coupons: { type: new GraphQLList(CouponType), resolve: resolvers.coupons },
    reviews: { type: new GraphQLList(ReviewType), resolve: resolvers.reviews },
    governorates: { type: new GraphQLList(GovernorateType), resolve: resolvers.governorates },
    settings: { type: new GraphQLList(SettingType), resolve: resolvers.settings },
  },
});

export const schema = new GraphQLSchema({ query: Query });