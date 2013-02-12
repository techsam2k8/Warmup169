require 'test_helper'

class UsersTest < ActiveSupport::TestCase
  test "LoginMethod" do
    controller = UsersController.new
    assert_respond_to(controller, 'login')
  end
  
  test "AddMethod" do
    controller = UsersController.new
    assert_respond_to(controller, 'add')
  end

  test "ResetMethod" do
    controller = UsersController.new
    assert_respond_to(controller, 'reset')
  end

  test "UnittestsMethod" do
    controller = UsersController.new
    assert_respond_to(controller, 'unittests')
  end
  
  test "CreateUser" do
    user = Users.create(:user => 'user', :password => 'password', :count => 1)
    assert_not_nil(Users.find(:first, :conditions => {:user => 'user'}))
  end
  
  test "ResetTable" do
    user = Users.create(:user => 'user', :password => 'password', :count => 1)
    Users.delete_all
    assert_nil(Users.find(:first, :conditions => {:user => 'user'}))
  end
  
  test "CheckPassword" do
    user = Users.create(:user => 'user', :password => 'password', :count => 1)
    assert_equal('password', Users.find(:first, :conditions => {:user => 'user'}).password)
  end
  
  test "CheckCount" do
    user = Users.create(:user => 'user', :password => 'password', :count => 1)
    assert_equal(1, Users.find(:first, :conditions => {:user => 'user'}).count)
  end

  test "UpdateCount" do
    user = Users.create(:user => 'user', :password => 'password', :count => 1)
    count = user.count + 1
    user.update_attribute(:count, count)
    assert_equal(2, Users.find(:first, :conditions => {:user => 'user'}).count)
  end
  
  test "UserColumnExists" do
    assert(Users.column_names.include?('user'))
  end

  test "PasswordColumnExists" do
    assert(Users.column_names.include?('password'))
  end
  
  test "CountColumnExists" do
    assert(Users.column_names.include?('count'))
  end
end
