require 'test_helper'

class UsersControllerTest < ActionController::TestCase
  test "should get client" do
    get :client
    assert_response :success
  end

end
