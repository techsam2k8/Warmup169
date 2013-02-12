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
  
  
end
