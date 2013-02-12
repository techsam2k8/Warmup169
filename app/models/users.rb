class Users < ActiveRecord::Base
  attr_accessible :count, :password, :user
  
  # validates :user, :uniqueness => true, :presence => true, :length => { :maximum => 128 }
  # validates :password, :length => { :maximum => 128 }
  
  # def self.login(user, password)
    # result = self.find(:first, :conditions => { :user => user, :password => password})
    # if result == nil
        # return -1
    # end
    # count = result.count + 1
    # result.update_attribute(:count, count)
    # return count
  # end
  
  # def self.add(user, password)
    # result = self.find(:first, :conditions => { :user => user })
    # if result != nil
        # return -2
    # end
    # if user == "" || user.length > 128
        # return -3
    # end
    # if password.length > 128
        # return -4
    # end
    # account = self.create(:user => user, :password => password, :count => 1)
    # return account.count
    
  # end
  
  # def self.TESTAPI_resetFixture()
    # self.delete_all
    # return 1
  # end
end
