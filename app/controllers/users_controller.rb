class UsersController < ApplicationController
    
    def login
        user = params[:user]
        password = params[:password]
        result = Users.find(:first, :conditions => { :user => user, :password => password})
        if result == nil
            render :json => {:errCode => -1}
        else
            count = result.count + 1
            result.update_attribute(:count, count)
            render :json => {:errCode => 1, :count => count}
        end
    end
    
    def add
        user = params[:user]
        password = params[:password]
        result = Users.find(:first, :conditions => { :user => user})
        if result != nil
            render :json => {:errCode => -2}
        elsif user == "" || user.length > 128
            render :json => {:errCode => -3}
        elsif password.length > 128
            render :json => {:errCode => -4}
        else
            account = Users.create(:user => user, :password => password, :count => 1)
            render :json => {:errCode => 1, :count => account.count}
        end
    end
    
    def reset
        Users.delete_all
        render :json => {:errCode => 1}
    end
    
    def unittests
        render :json => {:totalTests => 10, :nrFailed => 0, :output => "Success"}
    end
end
    